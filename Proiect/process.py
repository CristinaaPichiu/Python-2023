import os
import subprocess
import sys
import psutil


def help_specific_command(command):
    if command == "view":
        print("view: displays information about all running processes.")
    elif command == "suspend":
        print("suspend <PID>: suspends execution of the process with the specified PID.")
    elif command == "resume":
        print("resume <PID>: resumes execution of the process with the specified PID.")
    elif command == "kill":
        print("kill <PID>: stops the process with the specified PID.")
    elif command == "run":
        print("run <path> <arguments>: runs a new process with the specified path and arguments.")
    else:
        print(f"Command: '{command}' doesnt exists.")


def exists_command(command):
    try:
        list_commands = ["view", "suspend", "resume", "kill", "run", "help", "exit"]
        if command not in list_commands:
            raise ValueError("The command entered is not valid.")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def is_syntax_correct(command, args):
    try:
        if command == "view" and len(args) == 0:
            return True
        elif command == "help" and len(args) == 1:
            return True
        elif command in ["suspend", "resume", "kill"] and len(args) == 1 and args[0].isdigit():
            return True
        elif command == "run" and len(args) >= 1:
            return True
        elif command == "exit" and len(args) == 0:
            return True
        else:
            raise ValueError("Incorrect syntax for the specified command.")
    except Exception as e:
        print(f"Error: {e}")
        return False


def view_command():
    for process in psutil.process_iter():
        try:
            pid = process.pid
            if pid != 0 and psutil.pid_exists(pid):
                print("------------------------------------------------------------------------------------")
                print(f'Process Info for PID {pid}: ')
                print(f'  PID: {pid}')
                print(f'  Name: {process.name()}')
                print(f'  Path: {process.exe()}')
                print(f'  CPU Percent: {process.cpu_percent()}')
                variable = process.memory_info()
                print(f'  Memory Info: rss: {variable.rss}, vms: {variable.vms} ')
                print(f'  Create Time: {process.create_time()}')
                print(f'  Status: {process.status()}')
                print(f'  Username: {process.username()}')
                print(f'  Connections: {process.connections()}')
                print(f'  Number of Threads: {process.num_threads()}')
                print("------------------------------------------------------------------------------------")
        except psutil.NoSuchProcess as e:
            print(f"Error: Process with PID {pid} does not exist. {e}")
        except psutil.AccessDenied as e:
            print(f"Error: Access denied when fetching data for process with PID {pid}. {e}")
        except Exception as e:
            print(f"Error occuring during fetching data for process with PID {pid}: {e}")


def run_command(path, parameters):
    try:
        subprocess.run([path] + parameters)
        print("Process started succesfully. ")

    except Exception as e:
        print(f"Error: {e}")


def kill_command(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print("Process killed succesfully. ")
    except Exception as e:
        print(f"Error: {e}")

def suspend_command(pid):
    try:
        process = psutil.Process(pid)
        process.suspend()
        print(f"Process with pid {pid} is suspended. ")
    except Exception as e:
        print(f"Error: {e}")

def resume_command(pid):
    try:
        process = psutil.Process(pid)
        process.resume()
        print(f"Process with pid {pid} has been resumed. ")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":

    print("Comenzile disponibile sunt:")
    print("1. view")
    print("2. suspend <PID>")
    print("3. resume <PID>")
    print("4. kill <PID>")
    print("5. run <path> <parametri>")
    print("6. help <comanda>")
    print("7. exit")

    while True:
        user_input = input("Enter a command: ")
        if user_input.lower() == 'exit':
            break

        # impart comanda in cuvinte
        parts = user_input.split()

        #print(len(parts))
        # primul cuvant reprezinta comanda propriu-zisa
        command = parts[0]
        # celelalte cuvinte sunt argumentele comenzii

        argumente = parts[1:]

        if exists_command(command) and is_syntax_correct(command, argumente):
            if command == "help" and argumente:
                help_specific_command(argumente[0])
            if command == "view":
                view_command()

            if command == "run":
                run_command(parts[1], parts[2:])

            if command == "kill":
                kill_command(int(parts[1]))

            if command == "suspend":
                suspend_command(int(parts[1]))

            if command == "resume":
                resume_command(int(parts[1]))
