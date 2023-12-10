import os
import sys
import psutil


def get_command():
    try:
        command = sys.argv[1]
        list_commands = ["view", "suspend", "resume", "kill", "run"]
        if command not in list_commands:
            raise ValueError("Comanda introdusă nu este validă.")
        return command
    except IndexError:
        print("Trebuie să introduci una dintre comenzile: view, suspend, resume, kill, run, cu sintaxa potrivita!")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None


def is_syntax_correct(command, args):
    try:
        if command == "view" and not args:
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
    comanda = get_command()
    argumente = sys.argv[2:]

    if is_syntax_correct(comanda, argumente) and comanda == "view":
        view_command()
