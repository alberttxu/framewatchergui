import threading
import time

import pexpect


def monitor_output(process, outputfile):
    try:
        while True:
            char = process.read_nonblocking(timeout=None)
            if char != "\r":
                print(char, end="", file=outputfile)
    except pexpect.EOF:
        print(f"Stopping thread running {process.pid}")


def run_framewatcher_shipper(watch_dir, *pr_dirs):
    args = ["-nocom"]
    if watch_dir:
        args += ["-w", watch_dir]
    for pr_dir in pr_dirs:
        if pr_dir:
            args += ["-pr", pr_dir]
    print("Shipper command: framewatcher " + " ".join(args))
    return pexpect.spawn("framewatcher", args, encoding="utf-8")


def run_framewatcher_worker(
    watch_dir,
    binning,
    power,
    processed_dir,
    output,
    thumb,
    dtotal,
    gpu_id,
    num_threads,
    volt,
):
    args = []
    if watch_dir:
        args += ["-w", watch_dir]
    if binning:
        args += ["-bin", binning]
    if power:
        args += ["-po", power]
    if processed_dir:
        args += ["-pr", processed_dir]
    if output:
        args += ["-o", output]
    if thumb:
        args += ["-thumb", thumb]
    if dtotal:
        args += ["-dtotal", dtotal]
    if gpu_id:
        args += ["-gpu", gpu_id]
    if num_threads:
        args += ["-thr", num_threads]
    if volt:
        args += ["-volt", volt]

    print("Worker command: framewatcher " + " ".join(args))
    return pexpect.spawn("framewatcher", args, encoding="utf-8")


def start_shipper(log, watch_dir, *pr_dirs):
    shipper = run_framewatcher_shipper(watch_dir, *pr_dirs)

    shipper_thread = threading.Thread(
        target=monitor_output, args=(shipper, log), daemon=True
    )
    shipper_thread.start()
    print(f"Started shipper, id = {shipper.pid}")
    return shipper


def start_worker(log, *framewatcher_args):
    worker = run_framewatcher_worker(*framewatcher_args)
    worker_thread = threading.Thread(
        target=monitor_output, args=(worker, log), daemon=True
    )
    worker_thread.start()
    print(f"Started worker, id = {worker.pid}")
    return worker


def stop_processes(processes):
    for process in processes:
        try:
            process.send(chr(3))  # ctrl-c
        except OSError:
            process.terminate()
