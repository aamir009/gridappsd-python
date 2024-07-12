from gridappsd import GridAPPSD, DifferenceBuilder, utils, topics
import time

def on_message_callback(header, message):
    print(f"header: {header} message: {message}")

# Connection details
username = "app_user"
password = "1234App"
gapps = GridAPPSD(username=username, password=password)

assert gapps.connected

model_state = {
    "power_system_config": {
        "GeographicalRegion_name": "_24809814-4EC6-29D2-B509-7F8BFB646437",
        "SubGeographicalRegion_name": "_ABEB635F-729D-24BF-B8A4-E2EF268D8B9E",
        "Line_name": "_4F76A5F9-271D-9EB8-5E31-AA362D86F2C3"
    },
    "simulation_config": {
        "start_time": "1574177400",
        "duration": "120",
        "simulator": "GridLAB-D",
        "timestep_frequency": "1000",
        "timestep_increment": "1000",
        "run_realtime": "true",
        "simulation_name": "ieee8500",
        "power_flow_solver_method": "NR",
        "model_creation_config": {
            "load_scaling_factor": "1.0",
            "schedule_name": "ieeezipload",
            "z_fraction": "0.0",
            "i_fraction": "1.0",
            "p_fraction": "0.0",
            "randomize_zipload_fractions": "false",
            "use_houses": "false"
        }
    }
}

request = {
    "command": "new",
    "input": model_state
}

gapps.send(topics.REQUEST_SIMULATION, request)

# Wait for a while to receive messages
time.sleep(5)

gapps.disconnect()
