import time
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
from rich.layout import Layout
from rich.console import Console
from rich import box
from rich.columns import Columns
from control import control_cpu, control_disk, control_memory, control_temperatures, control_net
import time
from datetime import datetime, timedelta
import argparse
console = Console()

def parse_arguments():
    """Configura y procesa los argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(description="Monitor de Recursos del Sistema")
    
    parser.add_argument("-p", "--puertos", nargs='*', type=int, default=[],
                        help="Lista de puertos conocidos a ignorar en avisos.")
    parser.add_argument("-c", "--cpu", type=int, default=80,
                        help="Umbral de uso de CPU para avisos (defecto: 80).")
    parser.add_argument("-m", "--memory", type=int, default=80,
                        help="Umbral de uso de CPU para avisos (defecto: 80).")
    parser.add_argument("-t", "--temp", type=int, default=80,
                        help="Umbral de temperatura para avisos (defecto: 80).")
    parser.add_argument("-d", "--disk", type=int, default=80,
                        help="Umbral de uso de disco para avisos (defecto: 80).")
    
    #NO he sabido como implementarlo
    # parser.add_argument("-s", "--screen", action="store_true", default=False,
    #                     help="Si se indica, los logs se muestran por pantalla.")
    
    return parser.parse_args()

def create_bar(percent, color="bright_blue"):
    try:
        val = float(str(percent).replace('%', ''))
    except: val = 0.0
    
    # Colores btop: Gradiente de verde a rojo
    bar_color = "green"
    if val > 50: bar_color = "yellow"
    if val > 80: bar_color = "red"
    
    prog = Progress(
        BarColumn(bar_width=None, complete_style=bar_color, finished_style=bar_color),
        TextColumn(f"[{bar_color}]{val:>3.0f}%[/]")
    )
    prog.add_task("", total=100, completed=val)
    return prog

def get_cpu_panel(cpu_data):
    table = Table.grid(expand=True)
    table.add_row(" [bold cyan]CPU USAGE[/]")
    table.add_row(create_bar(cpu_data["CPU_usage"]))
    return Panel(table, title="[b]Proc[/]", border_style="cyan", box=box.HEAVY)

def get_mem_panel(mem_data):
    table = Table.grid(expand=True)
    # RAM
    table.add_row(f" [bold magenta]RAM[/] [dim]{mem_data['ram_total_gb']}GB[/]")
    table.add_row(create_bar(mem_data["ram_usage_percent"], "magenta"))
    # SWAP
    table.add_row(f"\n [bold yellow]SWAP[/] [dim]Ratio: {mem_data['swap_ratio']}[/]")
    table.add_row(create_bar(mem_data["swap_usage_percent"], "yellow"))
    
    msg = "[blink red]!! PRESSURE !![/]" if mem_data["pressure_warning"] else "[green]STATUS: OK[/]"
    table.add_row(f"\n {msg}")
    
    return Panel(table, title="[b]Mem[/]", border_style="magenta", box=box.HEAVY)

def get_sys_panel(disk_data, net_data):
    table = Table.grid(expand=True)
    # Disco
    table.add_row(f" [bold blue]DISK[/] [dim]{disk_data['used_gb']}/{disk_data['total_gb']}GB[/]")
    table.add_row(create_bar(disk_data["percent"], "blue"))
    
    # Red simple abajo
    table.add_row(f"\n [bold green]NET[/] [dim]Conns: {net_data['total_connections']}[/]")
    ports = ", ".join(map(str, net_data["open_ports"]))
    table.add_row(f" [white]Ports: {ports}[/]")
    
    return Panel(table, title="[b]Sys[/]", border_style="blue", box=box.HEAVY)

def get_temps(temp_data):
    table = Table.grid(expand=True)
    table.add_row(" [dark_orange]TEMPERATURES[/] ")

    if temp_data and "error" not in temp_data:
        for sensor, temperatura in temp_data.items():
            table.add_row(f" [bold dark_orange]{sensor}:[/] [bold white]{temperatura}ºC[/]")
    else:
        # Si hay error o está vacío
        msg = temp_data.get("error", "NO SE HAN ENCONTRADO SENSORES")
        table.add_row(f" [red]{msg}[/]")
    
    return Panel(table, title="[b]Sys[/]", border_style="dark_orange", box=box.HEAVY)

def make_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=1)
    )
    layout["main"].split_column(
        Layout(name="cpu"),
        Layout(name="memory"),
        Layout(name="system"),
        Layout(name="temps")
        
    )
    return layout

def main():
    layout = make_layout()
    datetime_ultimo_log = datetime.now()
    args = parse_arguments()
    with Live(layout, refresh_per_second=4, screen=True) as live:
        while True:
            datetime_actual = datetime.now()
            
            # Lógica de Logs cada 30 segundos
            log = (datetime_actual - datetime_ultimo_log).total_seconds() >= 30
            
            # Actualización de datos pasando los parámetros del CLI
            cpu = control_cpu(log, umbral=args.cpu)
            mem = control_memory(log, umbral=args.memory)
            disk = control_disk(log, umbral=args.disk)
            net = control_net(log, puertos=args.puertos)
            temperatures = control_temperatures(log, umbral=args.temp)

            if log:
                datetime_ultimo_log = datetime_actual

            # Update Layout
            layout["header"].update(Panel(" [bold white]VISUALIZADOR DE RECURSOS[/] [dim]|[/] [cyan]CPU[/] [magenta]MEM[/] [blue]DISK[/] [dark_orange]TEMPS[/]", style="white on black", box=box.SIMPLE))
            layout["cpu"].update(get_cpu_panel(cpu))
            layout["memory"].update(get_mem_panel(mem))
            layout["system"].update(get_sys_panel(disk, net))
            layout['temps'].update(get_temps(temperatures))
            layout["footer"].update(f"[bold white] Ultimo log: {datetime_ultimo_log.strftime('%m/%d/%Y, %H:%M:%S')} [/]")
            
            time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        console.clear()
        console.print("[bold red]Stopped.[/]")