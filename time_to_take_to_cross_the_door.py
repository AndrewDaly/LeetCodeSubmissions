# Create a global_clock object to keep track of the time
class Global_clock():
    def __init__(self, time):
    self.time = time
    def increment_clock_time(self):
        self.time = self.time + 1
    def set_time(self, time_to_begin_at):
        self.time = time_to_begin_at

class Door():
    def __init__(self):
        self.the_door_been_used_in_the_previous_second = False
        self.the_door_was_last_used_to_enter = False
        self.the_door_was_last_used_to_exit = False

# Create an exist queue to keep track of everyone in line to leave

class Exit_queue():
    def __init__(self):
        self.exit_list = []

# Create an entry queue to keep track of everyone in line to enter
# Thinking to have a person class as well if that turns out to be helpful
class Entry_queue():
    def __init__(self):
        self.entry_list = []

class person()
    def __init__(self, state, arrival_time):
        self.state = state
        self.arrival_time = arrival_time


class Solution(object):
    def timeTaken(self, arrival, state):
        """k
        :type arrival: List[int]
        :type state: List[int]
        :rtype: List[int]
        """
        # need to go in order of arrival
        # check if multiple people arrive at the same time
        # would need a global clock
        # at each door crossing the global clock increases
        # and more people can arrive in queue
        # need some handle queue function
        # need know the history of door crossing
        # t -1 door is unnused
        # t 0 door queues are initialized
        # t arrival[first_element] first set of people show up, either entering or leaving
        # door_handler admits one person, who's state gets updated, and the global clock increments
        # check if more people are queued up
        # run door_handler to admit one person from the queues
        # run until arrival[last_element] has been added to the queues, and queues are empty
        
        # Create our global clock object
        global_clock = Global_clock(0)
        entry_queue = Entry_queue()
        exist_queue = Exit_queue()

        # loop through the arrival array
        for i, j in enumerate(arrival):
            current_state_of_arrival = state[i]
            current_arrival = Person(current_state_of_arrival, arrival[i])

            # for the first arrival, initialize the clock time with the first arrival time
            if i == 0:
                global_clock.set_time(j)

            # Check if the current arrival is coming or going, and add to the relevant queue
            if current_arrival.state == 0:
                entry_queue.entry_list.append(person)
            else:
                exit_queue.exit_list.append(person)
            # now we need some additional logic in case multiple people arrive at the same time
            
            # check if there is another arrival
            if i < len(arrivals):
                next_arrival_time = arrivals[i+1]
                if next_arrival_time == current_arrival_time:
                    # move to next iteration of the loop and do not increment the global clock
                    # the next arrival needs to be added to the queues before any action is taken
                    # because multiple people can arrive at the same time we need some check
                    pass # will implement later
                else:
                    # the next arrival is not at the same time, we can process the queues
                