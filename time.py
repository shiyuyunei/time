import time

def focus_timer(total_time, break_time):
    while True:
        print(f"工作中... 专注 {total_time} 分钟")
        time.sleep(total_time * 60)  # 等待总专注时间（分钟）
        print("休息中... 请休息一下，放松一下。")
        time.sleep(break_time * 60)  # 等待休息时间（分钟）

if __name__ == "__main__":
    total_time = 25  # 设置总专注时间（分钟）
    break_time = 5   # 设置休息时间（分钟）
    focus_timer(total_time, break_time)
