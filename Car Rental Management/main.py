import tkinter as tk
from tkinter import ttk
class Main:
    def __init__(self):
        pass
    # ===============================
    available_vehicles: list = [
        {
            "vehicle" : "Bicycle", 
            "id" : 0, 
            "brand" : "Celt2k24",
            "model" : "Fixie", 
            "status" : "Available",
            "visible" : True,
        },
        {
            "vehicle" : "Motorcycle", 
            "id" : 11, 
            "brand" : "Honda",
            "model" : "XRM", 
            "status" : "Available",
            "visible" : True,
        },
    ]
        # ===============================
    def Program(self):
        # Root Window
        root = tk.Tk()
        root.title("Car Rental System")
        root.geometry("900x600")

        # Configure grid for main window (rows/columns)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)

        # ===============================
        # Top Navigation Bar
        # ===============================
        top_frame = ttk.Frame(root, padding=10)
        top_frame.grid(row=0, column=0, sticky="ew")
        top_label = ttk.Label(top_frame, text="Car Rental System", font=("Helvetica", 16, "bold"))
        top_label.pack(anchor="center")

        # ===============================
        # Main Content Area
        # ===============================
        main_frame = ttk.Frame(root, padding=10)
        main_frame.grid(row=1, column=0, sticky="nsew")
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=2)
        main_frame.rowconfigure(0, weight=1)
        # ===============================
        # Left Panel – Vehicle Selection
        # ===============================
        vehicle_selection_frame = ttk.LabelFrame(main_frame, text="Select Vehicle", padding=10)
        vehicle_selection_frame.grid(row=0, column=0, sticky="nswe", padx=(0, 10))

        ttk.Label(vehicle_selection_frame, text="Vehicle Type:").pack(anchor="w", pady=(0, 5))
        vehicle_type_combo = ttk.Combobox(vehicle_selection_frame, values=self.available_vehicles[0]["vehicle"])
        vehicle_type_combo.pack(fill="x", pady=(0, 10))

        search = ttk.Button(vehicle_selection_frame, text="Search", command=lambda: self.show_selected_vehicle(vehicle_type_combo.get()) ).pack(fill="x")

        # ===============================
        # Right Panel – Dashboard
        # ===============================
        dashboard_frame = ttk.LabelFrame(main_frame, text="Available Vehicles", padding=10)
        dashboard_frame.grid(row=0, column=1, sticky="nsew")

        # Treeview for vehicle list
        columns = ("vehicle", "id", "brand", "model", "status")
        vehicle_tree = ttk.Treeview(dashboard_frame, columns=columns, show="headings", height=15)

        for col in columns:
            vehicle_tree.heading(col, text=col)
            vehicle_tree.column(col, width=100)
            
        vehicle_tree.pack(fill="both", expand=True)

        # Display vehicles
        for vehicle in self.available_vehicles:
            if vehicle["visible"] == True:
                column = (vehicle["vehicle"], vehicle["id"], vehicle["brand"], vehicle["model"], vehicle["status"])
                vehicle_tree.insert('', 'end', values=column)
                print(vehicle)

        # ===============================
        # Bottom Status Bar (optional)
        # ===============================
        status_bar = ttk.Label(root, text="Ready", relief="sunken", anchor="w", padding=5)
        status_bar.grid(row=2, column=0, sticky="ew")

        # Start mainloop
        root.mainloop()

    def show_selected_vehicle(self, searched_vehicle):
        for vehicle in self.available_vehicles:
            if vehicle["vehicle"] != searched_vehicle:
                vehicle["visible"] = False
                print(vehicle["visible"])
        
        

main = Main()
main.Program()