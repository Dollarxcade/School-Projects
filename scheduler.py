import pandas as pd
import os
import re

def parse_complex_dates(date_str):
    if pd.isna(date_str) or "can't attend" in str(date_str).lower():
        return []
    pattern = r',(?=\s*(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday))'
    dates = re.split(pattern, str(date_str))
    return [d.strip() for d in dates if d.strip()]

def generate_schedule():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv') and f != 'final_volunteer_schedule.csv']
    
    if not csv_files:
        print("Error: No CSV file found.")
        return
    
    file_path = os.path.join(current_dir, csv_files[0])
    df = pd.read_csv(file_path)
    
    data = pd.DataFrame({
        'timestamp': pd.to_datetime(df.iloc[:, 0]),
        'email': df.iloc[:, 1],
        'name': df.iloc[:, 2],
        'vol_dates_raw': df.iloc[:, 4],
        'train_dates_raw': df.iloc[:, 5],
        'grade': pd.to_numeric(df.iloc[:, 6], errors='coerce')
    })

    data = data.sort_values('timestamp').drop_duplicates('email', keep='last')
    data['vol_dates'] = data['vol_dates_raw'].apply(parse_complex_dates)
    data['train_dates'] = data['train_dates_raw'].apply(parse_complex_dates)
    data = data[data['vol_dates'].map(len) > 0]
    
    data['flexibility_score'] = data['vol_dates'].apply(len)
    data['assignment_count'] = 0

    num_groups_per_day = int(input("How many groups per day? "))
    people_per_group = int(input("How many people per group? "))
    max_sessions = int(input("Max sessions allowed per person? "))

    all_dates = sorted(list(set(d for sublist in data['vol_dates'] for d in sublist)))
    schedule_dict = {date: [[] for _ in range(num_groups_per_day)] for date in all_dates}
    training_track = {date: {i: None for i in range(num_groups_per_day)} for date in all_dates}

    optimized_volunteers = data.sort_values(by=['flexibility_score', 'grade'])

    for _, volunteer in optimized_volunteers.iterrows():
        if not volunteer['train_dates']:
            continue

        assigned_total = 0
        for target_date in volunteer['vol_dates']:
            if assigned_total >= max_sessions:
                break
                
            placed = False
            for g_idx in range(num_groups_per_day):
                current_group = schedule_dict[target_date][g_idx]
                if len(current_group) >= people_per_group:
                    continue
                
                v_train = set(volunteer['train_dates'])
                group_train_pool = training_track[target_date][g_idx]
                
                if group_train_pool is None:
                    schedule_dict[target_date][g_idx].append(volunteer)
                    training_track[target_date][g_idx] = v_train
                    assigned_total += 1
                    placed = True
                    break
                else:
                    intersect = group_train_pool & v_train
                    if intersect:
                        schedule_dict[target_date][g_idx].append(volunteer)
                        training_track[target_date][g_idx] = intersect
                        assigned_total += 1
                        placed = True
                        break
            if placed: continue

    final_rows = []
    for date in all_dates:
        assigned_emails_today = []
        for g_idx in range(num_groups_per_day):
            group = schedule_dict[date][g_idx]
            train_date = list(training_track[date][g_idx])[0] if training_track[date][g_idx] else "N/A"
            
            if 0 < len(group) < people_per_group:
                print(f"Warning: {date} - Group {g_idx+1} only has {len(group)}/{people_per_group} people.")

            for member in group:
                assigned_emails_today.append(member['email'])
                final_rows.append({
                    "Volunteer Date": date,
                    "Status": "Assigned",
                    "Reason for Unassigned": "N/A",
                    "Group Number": f"Group {g_idx+1}",
                    "Required Training Date": train_date,
                    "Name": member['name'],
                    "Grade": member['grade'],
                    "Email": member['email']
                })
        
        daily_pool = data[data['vol_dates'].apply(lambda x: date in x)]
        unassigned = daily_pool[~daily_pool['email'].isin(assigned_emails_today)]
        
        for _, leftover in unassigned.iterrows():
            total_assigned = len([r for r in final_rows if r['Email'] == leftover['email'] and r['Status'] == 'Assigned'])
            
            if not leftover['train_dates']:
                reason = "No Training Availability ('Can't attend')"
            elif total_assigned >= max_sessions:
                reason = f"Max Sessions Reached ({max_sessions})"
            else:
                reason = "Group Capacity Full / Training Mismatch"

            final_rows.append({
                "Volunteer Date": date,
                "Status": "Unassigned",
                "Reason for Unassigned": reason,
                "Group Number": "N/A",
                "Required Training Date": "N/A",
                "Name": leftover['name'],
                "Grade": leftover['grade'],
                "Email": leftover['email']
            })

    output_df = pd.DataFrame(final_rows)
    output_df = output_df.sort_values(by=['Volunteer Date', 'Status'], ascending=[True, True])
    
    output_path = os.path.join(current_dir, "final_volunteer_schedule.csv")
    output_df.to_csv(output_path, index=False)
    print(f"\nDone! Output saved to local folder.")
    print(f"Saved to: {output_path}")

if __name__ == "__main__":
    generate_schedule()