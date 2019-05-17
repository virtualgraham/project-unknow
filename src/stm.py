# State Transition Model - STM

# a transition count matrix keeps a count of transitions from training sequences
# sum_transition_count - used to calculate transtion probabilities on the fly
# or to build normalised trantion matrix

# a simple STM models the probability of the next state given the current state
# P(x(t+1)|x(t)) or simple a markov process

# a generic STM models the probability of the next state given n number of
# conditional values.
# P(x(t+1)|c1, c2, c3...., cn)
# for example P(x(t+1)|x(t), x(t-1), x(t-2))
# or P(x(t+1)|ELAPSED_TIME_SINCE(x == x(t))

# perhaps there is a way to build an STM with transtion probibilites that
# are inspired LSTM RNN techniques


class stm():

    def __init__(self, state_count, *cond_counts):
        self.state_count = state_count
        # create transition count matrix of size [state_count, cond_counts[0], cond_counts[1], ...]

    # get probability that a sequence could be generated by this model
    def seq_prob(self, s):
        return 0.0

    # update (train) transition probilities by adding a sample transition to
    # the trasnition count matrix
    # v is a vector with v[0] the new state
    # and v[1], v[2]... being condtional values
    def add_transition(self, v):
        # increments trantion count matrix at [v0, v1..]
        return
