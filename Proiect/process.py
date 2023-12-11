import os
import subprocess
import sys
import psutil

def help_specific_command(command):
    if command == "view":
        print("view: Afișează informații despre toate procesele în execuție.")
    elif command == "suspend":
        print("suspend <PID>: Suspendă execuția procesului cu PID-ul specificat.")
    elif command == "resume":
        print("resume <PID>: Reia execuția procesului cu PID-ul specificat.")
    elif command == "kill":
        print("kill <PID>: Termină procesul cu PID-ul specificat.")
    elif command == "run":
        print("run <path> <arguments>: Rulează un nou proces cu path-ul si argumentele specificate.")
    else:
        print(f"Comanda '{command}' nu exista.")


def exists_command(command):
    try:
        list_commands = ["view", "suspend", "resume", "kill", "run", "help"]
        if command not in list_commands:
            raise ValueError("Comanda introdusă nu este validă.")
        return True  # Comanda există în listă
    except ValueError as e:
        print(f"Error: {e}")
        return False  # Comanda nu există în listă
    except Exception as e:
        print(f"Error: {e}")
        return False  # În caz de altă excepție, comanda nu există în listă



def is_syntax_correct(command, args):
    try:
        if command == "view" and not args:
            return True
        elif command == "help" and len(args) == 1:
            return True
        elif command in ["suspend", "resume", "kill"] and len(args) == 1 and args[0].isdigit():
            return True
        elif command == "run" and len(args) == 2 and os.path.isfile(args[0]):
            return True
        else:
            raise ValueError("Sintaxă incorectă pentru comanda specificată.")
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def view_command():
    for process in psutil.process_iter():
        try:
            pid = process.pid
            if pid != 0 and psutil.pid_exists(pid):
                print("-" * 60)
                print(f'Process Info for PID {pid}: ')
                print(f'  PID: {pid}')
                print(f'  Name: {process.name()}')
                print(f'  CPU Percent: {process.cpu_percent()}')
                print(f'  Memory Info: {process.memory_info()}')
                print(f'  Create Time: {process.create_time()}')
                print(f'  Status: {process.status()}')
                print(f'  Username: {process.username()}')
                print(f'  Connections: {process.connections()}')
                print(f'  Number of Threads: {process.num_threads()}')
                print("-" * 60)
        except psutil.NoSuchProcess as e:
            print(f"Error: Process with PID {pid} does not exist. {e}")
        except psutil.AccessDenied as e:
            print(f"Error: Access denied when fetching data for process with PID {pid}. {e}")
        except Exception as e:
            print(f"Error occuring during fetching data for process with PID {pid}: {e}")


if __name__ == "__main__":
    print("Comenzile disponibile sunt:")
    print("1. view")
    print("2. suspend <PID>")
    print("3. resume <PID>")
    print("4. kill <PID>")
    print("5. run <path> <parametri>")
    print("6. help <comanda>")
    while True:
        user_input = input("Introdu o comandă sau 'exit' pentru a ieși: ")
        if user_input.lower() == 'exit':
            break

        # impart comanda in cuvinte
        parts = user_input.split()
        # primul cuvant reprezinta comanda propriu-zisa
        command = parts[0]
        # celelalte cuvinte sunt argumentele comenzii
        argumente = parts[1:]


        if exists_command(command) and is_syntax_correct(command, argumente):
            if command == "help" and argumente:
                help_specific_command(argumente[0])
            if command == "view":
                 view_command()

