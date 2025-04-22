import time
from playsound import playsound

def countdown(minutes, label="Work"):
    seconds = minutes * 60
    print(f"\n🔔 {label} timer started for {minutes} minutes.")

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ {label} | {timer_display}", end="")
        time.sleep(1)
        seconds -= 1

    print(f"\n✅ {label} session finished!")
    try:
        playsound("sounds/alarm.wav")
    except:
        print("🔕 Sound failed (optional)")

def pomodoro_cycle(work=25, short_break=5, cycles=4):
    for i in range(1, cycles + 1):
        print(f"\n🍅 Pomodoro #{i}")
        countdown(work, label="Work")
        if i < cycles:
            countdown(short_break, label="Break")
    print("\n🏁 All pomodoro cycles completed!")
