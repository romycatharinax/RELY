# Functionaliteit van Romy.
# Deze functionaliteit bevat geen CPU_usage meer.
# psutil is een platformonafhankelijke bibliotheek voor het ophalen van informatie over actieve processen en systeemgebruik in Python.


import psutil
from datetime import datetime
import tabulate
import logging


logging.basicConfig(filename='Logging_example3.0.txt', format='%(name)s:%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', filemode='w', level=logging.DEBUG)
logging.info('This file includes info of the steps that the program makes.')
logging.info('Program is getting process id (pid), Process ID:')
logging.info('Program is getting process name (name)')
logging.info('Program is getting process creation time (create_time)')
logging.info('Program is getting cores used by the process (cores)')
logging.info('Program is getting the status of the process (status)')
logging.info('Program is getting information about memory used by the process (memory_usage)')
logging.info('Program is getting read bytes used by the process (read_bytes)')
logging.info('Program is getting written bytes used by the process (write_bytes)')
logging.info('Program is getting threads used by the process (treads)')
logging.info('Program is getting the username related to the process (username)')
logging.info('Program is getting the path of the process (path)')
logging.info('Program got all the information.')
logging.info('The output of the program is being saved in a file.')
logging.info('The output of the program has been saved to a file.')

def proces_list():
    # Lijst die alle proces dictionaries bevat.
    processes = []
    for process in psutil.process_iter():

        # Verkrijg alle proces informatie met one shot. Hulpprogramma context manager die het ophalen van meerdere procesinformatie tegelijkertijd aanzienlijk versnelt
        with process.oneshot():
            # Verkrijgen van het proces ID.
            pid = process.pid
            logging.info('Program is getting process id (pid):', pid.str())
            # Naam verkrijgen van het uitgevoerde bestand.
            name = process.name()
            # Tijd verkrijgen van wanneer het proces gecreeerd is.
            create_time = datetime.fromtimestamp(process.create_time())
            try:
                # Verkrijg het aantal CPU-cores dat dit proces kan uitvoeren.
                cores = len(process.cpu_affinity())
            except psutil.AccessDenied:
                cores = 0
            # Verkrijg de status van het proces.
            status = process.status()
            try:
                # Verkrijgen van het geheugen gebruik in bytes.
                memory_usage = process.memory_full_info().uss
            except psutil.AccessDenied:
                memory_usage = 0
            # Totale proces gelezen en geschreven bytes.
            io_counters = process.io_counters()
            read_bytes = io_counters.read_bytes
            write_bytes = io_counters.write_bytes
            # Het ophalen van het aantal totale threads dat door het proces wordt voortgebracht
            n_threads = process.num_threads()
            # Ontvang de gebruikersnaam van gebruiker die het proces heeft voortgebracht
            try:
                username = process.username()
            except psutil.AccessDenied:
                username = "N/A"
            logging.info('Program is getting the username related to the process (username): '), username
            try:
                path = process.exe()
            except psutil.AccessDenied:
                path = "-"
        processes.append({
            'pid': pid, 'name': name, 'create_time': create_time,
            'cores': cores, 'status': status, 'memory_usage': memory_usage,
            'read_bytes': read_bytes, 'write_bytes': write_bytes,
            'n_threads': n_threads, 'username': username, 'path': path,
        })

    # print(processes)

    save_file(processes)


def save_file(processes):

    # print(processes)

    # Hiermee wordt de lijst netjes weergegeven in de console.
    header = processes[0].keys()
    rows = [x.values() for x in processes]
    tableproceslist = tabulate.tabulate(rows, header, tablefmt='rst')
    print(tableproceslist)

    # Hiermee wordt de lijst met uitkomsten opgeslagen in een .txt bestand.
    f = open('C://Users/romyw/Documents/ipfit5/Proces_list.txt', 'w')  # extern opslaan
    # f = open('Proces_list.txt', 'w')  # intern opslaan
    f.write(tableproceslist)
    f.close()


def main():
    proces_list()


if __name__ == '__main__':
    main()
