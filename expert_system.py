class ExpertSystem:
    def __init__(self):
        self.hospitals = {
            "General Hospital": {
                "Location": "123 Main Street",
                "Specialty": "General Medicine, Emergency Care",
                "Rating": 4.5,
            },
            "Children's Hospital": {
                "Location": "456 Elm Street",
                "Specialty": "Pediatrics, Neonatology",
                "Rating": 4.8,
            },
            "Regional Medical Center": {
                "Location": "789 Oak Street",
                "Specialty": "Surgery, Oncology",
                "Rating": 4.3,
            },
        }

    def ask_questions(self):
        print("Welcome to the Hospital Expert System!")
        print("I'll help you find the best hospital or medical facility based on your needs.")

        print("\nWhat type of medical service are you looking for?")
        service = input("Enter 'general', 'pediatrics', 'surgery', 'emergency', or 'oncology': ").lower()

        print("\nDo you have a preference for hospital location?")
        location_preference = input("Enter 'yes' or 'no': ").lower()

        if location_preference == "yes":
            print("\nWhat is your preferred location?")
            preferred_location = input("Enter a city or area: ")
        else:
            preferred_location = None

        self.find_hospital(service, preferred_location)

    def find_hospital(self, service, preferred_location):
        matching_hospitals = []

        for name, info in self.hospitals.items():
            if service in info["Specialty"].lower():
                if preferred_location:
                    if preferred_location.lower() in info["Location"].lower():
                        matching_hospitals.append((name, info["Location"], info["Rating"]))
                else:
                    matching_hospitals.append((name, info["Location"], info["Rating"]))

        if matching_hospitals:
            print("\nHere are the hospitals that match your criteria:")
            for hospital in matching_hospitals:
                print(f"\nHospital: {hospital[0]}")
                print(f"Location: {hospital[1]}")
                print(f"Rating: {hospital[2]}")
        else:
            print("\nSorry, we couldn't find any hospitals matching your criteria.")

def main():
    expert_system = ExpertSystem()
    expert_system.ask_questions()

if __name__ == "__main__":
    main()
