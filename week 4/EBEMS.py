# E-Business Event Management System

# Event Database (Using dictionaries)
events = {}

# Customer Loyalty Points Database
loyalty_points = {}

# Variable to store the current event ID
current_event = None

# Function to create a new event
def create_event(event_id, event_name, speaker, date, time, topic, capacity):
    global current_event  # Use the global keyword to modify the global variable
    events[event_id] = {
        'event_name': event_name,
        'speaker': speaker,
        'date': date,
        'time': time,
        'topic': topic,
        'capacity': capacity,
        'attendees': [],
        'feedback': [],
    }
    current_event = event_id  # Set the current event to the newly created event
    print(f"Event {event_name} created successfully.") # if created successfully, print it out.

# Function to display event details
def display_event_details():
    global current_event  # Use the global keyword to access the global variable
    if current_event in events: # try to judge whether the current event is in the event or not
        event_info = events[current_event] # event information included
        print(f"Event ID: {current_event}")
        print(f"Event Name: {event_info['event_name']}")
        print(f"Speaker: {event_info['speaker']}")
        print(f"Date: {event_info['date']}")
        print(f"Time: {event_info['time']}")
        print(f"Topic: {event_info['topic']}")
        print(f"Capacity: {event_info['capacity']}")
        print(f"Registered Attendees: {len(event_info['attendees'])}")
    else:
        print("Event not found.") # if the event not found

# Function to register for an event
def register_for_event(customer_name):
    global current_event  # Use the global keyword to access the global variable
    if current_event in events:
        event_info = events[current_event]
        if len(event_info['attendees']) < event_info['capacity']: # judge whether the number of participants is smaller then the capacity
            event_info['attendees'].append(customer_name) # if it's, add the customer's name to ensure he/she will attend
            
            # Loyalty points increment for each registration
            loyalty_points[customer_name] = loyalty_points.get(customer_name, 0) + 1 # every time customer attends, their loyalty will also increase by one
            
            print(f"Registration successful for {customer_name} in {event_info['event_name']}.") # customer registratd successfully will be in the event
        else:
            print(f"Registration failed. Event {event_info['event_name']} is at full capacity.") # if failed, he/she will not be in the event
    else:
        print("Event not found.")

# Function to provide post-event feedback
def provide_feedback(customer_name, rating, comments):
    global current_event  # Use the global keyword to access the global variable
    if current_event in events:
        event_info = events[current_event]
        feedback_entry = {'customer_name': customer_name, 'rating': rating, 'comments': comments} # provide information about feedback, including name, rating and comments
        event_info['feedback'].append(feedback_entry) # add in feedback info
        print(f"Feedback submitted successfully for {event_info['event_name']}.") # if submitted successfully, print it out
    else:
        print("Event not found.")

# Function to generate a report on event attendance, feedback and attendance rate
def generate_event_report():
    global current_event  # Use the global keyword to access the global variable
    if current_event in events:
        event_info = events[current_event]
        total_attendees = len(event_info['attendees']) # the number of total attendees
        attendance_rate = (total_attendees / event_info['capacity']) * 100 if event_info['capacity'] > 0 else 0   # calcualte the attendance rate

        print(f"Event Report for {event_info['event_name']}:")
        print(f"Total Attendance: {total_attendees}")  # print the total attendees
        print(f"Attendance Rate: {attendance_rate:.2f}%") # print the attendance rate
        print("Feedback:") # print feedback
        for feedback_entry in event_info['feedback']:
            print(f"   - {feedback_entry['customer_name']}: {feedback_entry['rating']} stars - {feedback_entry['comments']}")  #print feedbadk including customer name, rating and comments
    else:
        print("Event not found.")

# Function to display loyalty points for each customer
def display_loyalty_points():
    print("Loyalty Points:")  # print loyalty points
    for customer, points in loyalty_points.items():  # check whether it in loyalty_ points.items
        print(f"   - {customer}: {points} points")

# User Interface
while True: # if true, print below content
    print("\nE-Business Event Management System:")
    print("1. Create Event")
    print("2. Display Event Details")
    print("3. Register for Event")
    print("4. Provide Feedback")
    print("5. Generate Event Report")
    print("6. Display Loyalty Points")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")  # input your the content of your choice

    if choice == '1': # choice 1 for adding basic info
        event_id = input("Enter event ID: ")
        event_name = input("Enter event name: ")
        speaker = input("Enter speaker's name: ")
        date = input("Enter event date: ")
        time = input("Enter event time: ")
        topic = input("Enter event topic: ")
        capacity = int(input("Enter event capacity: "))
        create_event(event_id, event_name, speaker, date, time, topic, capacity)

    elif choice == '2':  # for displaying event's details
        display_event_details()

    elif choice == '3':  # for checking whether registering
        if current_event is not None:
            customer_name = input("Enter your name: ")
            register_for_event(customer_name)
        else:
            print("No event selected. Please create or choose an event first.")

    elif choice == '4':  # provide info about feedback report
        if current_event is not None:
            customer_name = input("Enter your name: ")
            rating = int(input("Enter your rating (1-5): "))
            comments = input("Enter your comments: ")
            provide_feedback(customer_name, rating, comments)
        else:
            print("No event selected. Please create or choose an event first.")

    elif choice == '5':  #generate report
        if current_event is not None:
            generate_event_report()
        else:
            print("No event selected. Please create or choose an event first.")

    elif choice == '6':  # get loyalty points
        display_loyalty_points()

    elif choice == '7': # for exiting
        print("Exiting the system. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
