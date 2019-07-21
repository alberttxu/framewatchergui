from gui import initGUI
from run import start_shipper, start_worker
from log import LogWindowWriter

window = initGUI()

try:
    while True:
        event, values = window.Read()

        if event == "Start":
            print("starting framewatcher session")
            window.Element("Start").Update(disabled=True)
            window.Element("Stop").Update(disabled=False)
            shipper_log = LogWindowWriter(window, "shipper_log")
            shipper = start_shipper(shipper_log)
            worker1_log = LogWindowWriter(window, "worker1_log")
            worker = start_worker(worker1_log)

        elif event == "Stop":
            print("stopping session")
            window.Element("Start").Update(disabled=False)
            window.Element("Stop").Update(disabled=True)
            worker.terminate()
            shipper.terminate()

        elif event == "Close" or event is None:
            print("closing gui")
            window.Close()
            worker.terminate()
            shipper.terminate()
            break

except KeyboardInterrupt:
    print("received keyboard interrupt; closing")
