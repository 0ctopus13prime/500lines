from collections import namedtuple

Proposal = namedtuple('Proposal', ['caller', 'client_id', 'input'])
Ballot = namedtuple('Ballot', ['view_id', 'n', 'leader'])
ScoutId = namedtuple('ScoutId', ['address', 'ballot_num'])
CommanderId = namedtuple('CommanderId', ['address', 'slot', 'proposal'])
ViewChange = namedtuple('ViewChange', ['view_id', 'peers'])

HEARTBEAT_INTERVAL = 0.5
HEARTBEAT_GONE_COUNT = 3
JOIN_RETRANSMIT = 0.7
CATCHUP_INTERVAL = 0.6
ACCEPT_RETRANSMIT = 1
PREPARE_RETRANSMIT = 1
ALPHA = 10

# replicas should be able to re-propose a view change before the new node
# re-transmits the JOIN
assert CATCHUP_INTERVAL < JOIN_RETRANSMIT


def view_primary(view_id, peers):
    return peers[view_id % len(peers)]

from .ship import Ship
