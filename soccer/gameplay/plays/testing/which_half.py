import robocup
import constants
import play
import enum
import behavior
import main

# Slides and other materials can be found here:
# https://github.com/RoboJackets/robocup-training
#
# Field Documentation can be found here:
# https://robojackets.github.io/robocup-software/struct_field___dimensions.html
#
# Ball Documentation can be found here:
# https://robojackets.github.io/robocup-software/class_ball.html


# Maintains the state of the ball's position by keeping track of which
# half the ball is on and prints on both entering a given state and
# continously during the execution of a given state.
class WhichHalf(play.Play):
    class State(enum.Enum):
        # Define your states here.
        # eg: some_state = 0
        # -----------------------
        topHalf = 0
        bottomHalf = 1
        

    def __init__(self):
        super().__init__(continuous=True)

        # Register the states you defined using 'add_state'.
        # eg: self.add_state(WhichHalf.State.<???>,
        #                    behavior.Behavior.State.running)
        # ----------------------------------------------------
        

        self.add_state(WhichHalf.State.topHalf, behavior.Behavior.State.running)
        self.add_state(WhichHalf.State.bottomHalf, behavior.Behavior.State.running)

        # Add your state transitions using 'add_transition'.
        # eg: self.add_transition(behavior.Behavior.State.start,
        #                         self.State.<???>, lambda: True,
        #                         'immediately')
        # eg: self.add_transition(self.State.<???>, self.State.<???>,
        #                         lambda: <???>,
        #                         'state change message')
        # ------------------------------------------------------------

        self.add_transition(behavior.Behavior.State.start,
        	self.State.topHalf, lambda: True, 'immediately'
        	)
        self.add_transition(self.State.topHalf, self.State.bottomHalf, lambda: main.ball().pos.y < constants.Field.Length/2, 'bottom half')
        self.add_transition(self.State.bottomHalf, self.State.topHalf, lambda: main.ball().pos.y > constants.Field.Length/2, 'top half')
        # Define your own 'on_enter' and 'execute' functions here.
        # eg: def on_enter_<???>(self):
        #         print('Something?')
        # eg: def execute_<???>(self):
        #         print('Something?')
        # ---------------------------------------------------------

    def on_enter_topHalf(self):
    	print("Now in top half")

    def on_enter_bottomHalf(self):
    	print("Now in bottom half")
		