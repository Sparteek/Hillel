from datetime import datetime
import logging


KEY = "Key TSTFEED0300|7E3E|0400"


logging.basicConfig(
    filename="hb_test.log",
    filemode="w",
    level=logging.WARNING,
    format="%(levelname)s: %(message)s",
)


def filter_log(file_name):
    filtered_log = []

    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            if KEY in line:
                filtered_log.append(line.strip())

    return filtered_log


def get_time(log_line):
    timestamp_position = log_line.find("Timestamp ")
    time_string = log_line[timestamp_position + 10:timestamp_position + 18]

    return datetime.strptime(time_string, "%H:%M:%S")


def analyze_heartbeat(filtered_log):
    for index in range(len(filtered_log) - 1):
        current_time = get_time(filtered_log[index])
        next_time = get_time(filtered_log[index + 1])

        heartbeat = current_time - next_time
        heartbeat_seconds = heartbeat.total_seconds()

        if 31 < heartbeat_seconds < 33:
            logging.warning(
                f"Heartbeat: {heartbeat_seconds} seconds, "
                f"time: {current_time.strftime('%H:%M:%S')}"
            )

        elif heartbeat_seconds >= 33:
            logging.error(
                f"Heartbeat: {heartbeat_seconds} seconds, "
                f"time: {current_time.strftime('%H:%M:%S')}"
            )


filtered_log = filter_log("hblog.txt")

print("Знайдено рядків:", len(filtered_log))

analyze_heartbeat(filtered_log)

print("Аналіз завершено. Результат записано в hb_test.log")