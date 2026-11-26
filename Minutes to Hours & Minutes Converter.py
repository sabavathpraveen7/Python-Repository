def format_minutes_to_hours(total_minutes):
    # // gets whole hours; % gets the leftover minutes
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    
    print(f"{total_minutes} minutes = {hours} hour(s) and {remaining_minutes} minute(s)")
    return hours, remaining_minutes

# Example usage:
# format_minutes_to_hours(145)
