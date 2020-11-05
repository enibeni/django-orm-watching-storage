

def format_duration(duration):
    m, s = divmod(int(duration), 60)
    h, m = divmod(m, 60)
    formatted_duration = f"{h}ч {m}мин"
    return formatted_duration