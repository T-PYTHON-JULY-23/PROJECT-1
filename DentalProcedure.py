class DentalProcedure:
    def __init__(self, procedure_name):
        self.procedure_name = procedure_name
        self.anesthesia_type = None
    
    def set_local_anesthesia(self):
        self.anesthesia_type = "Local Anesthesia"
    
    def set_full_anesthesia(self):
        self.anesthesia_type = "Full Anesthesia"

    def perform_procedure(self):
        if self.anesthesia_type == "Local Anesthesia":
            self.perform_local_anesthesia()
        
        # Perform the dental procedure here

    def perform_local_anesthesia(self):
        # Code to administer local anesthesia
        print("Local anesthesia administered.")

    def perform_full_anesthesia(self):
        # Code to administer full anesthesia
        print("Full anesthesia administered.")

