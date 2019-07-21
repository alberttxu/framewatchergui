import threading
import time

import pexpect


def monitor_output(process, outputfile):
    try:
        while True:
            char = process.read_nonblocking(timeout=None)
            # print(bytes(char, 'utf-8'), end=' ')
            if char != "\r":
                print(char, end="", file=outputfile)
    except pexpect.EOF:
        print(f"stopping thread running {process.pid}")


def run_framewatcher_shipper(watch_dir, *dest_dirs):
    args = ["-nocom", "-w", watch_dir]
    for dest_dir in dest_dirs:
        args += ["-pr", dest_dir]
    print("shipper command: framewatcher " + " ".join(args))
    return pexpect.spawn("framewatcher", args, encoding="utf-8")


def run_framewatcher_worker(
    watch_dir,
    binning,
    power,
    processed,
    output,
    thumb,
    dtotal,
    gpu,
    threads,
    volt,
):
    args = [
        "-w",
        watch_dir,
        "-bin",
        binning,
        "-po",
        power,
        "-pr",
        processed,
        "-o",
        output,
        "-thumb",
        thumb,
        "-dtotal",
        dtotal,
        "-gpu",
        gpu,
        "-thr",
        threads,
        "-volt",
        volt,
    ]

    print("worker command: framewatcher " + " ".join(args))
    return pexpect.spawn("framewatcher", args, encoding="utf-8")


def start_shipper(log):
    shipper = run_framewatcher_shipper("/tmp", "/tmp/tmp2")

    shipper_thread = threading.Thread(
        target=monitor_output, args=(shipper, log), daemon=True
    )
    shipper_thread.start()
    print(f"started shipper, id = {shipper.pid}")
    return shipper


def start_worker(log):
    worker = run_framewatcher_worker(
        "/tmp", "2", "1024", "/tmp", "/tmp", "/tmp", "45", "-1", "1", "300"
    )
    worker_thread = threading.Thread(
        target=monitor_output, args=(worker, log), daemon=True
    )
    worker_thread.start()
    print(f"started worker, id = {worker.pid}")
    return worker
