### RUBY VERSION ###
# def jesse(tickets, p)
#     jesses_place = p
#     jesses_tickets = tickets[p-1]
#     less = 0 # difference of all ticket less than jesse
#     behind = 0 # number of people beind jesse
#     tickets.each_with_index do |their_tickets, index| 
#         if index < jesses_place
#             if their_tickets < jesses_tickets
#                 less += (jesses_tickets - their_tickets) 
#             end
#         else
#             if their_tickets < (jesses_tickets - 1)
#                 less += (jesses_tickets - (their_tickets - 1)) 
#             end
#             behind += 1
#         end
#     end
#     (tickets.size * jesses_tickets) - (less + behind)
# end
# jesse([5,3,2,1,4,3,7], 5)

def jesse(tickets, p):
    jesses_place = p
    jesses_tickets = tickets[p-1]
    less = 0 # difference of all ticket less than jesse
    behind = 0 # number of people beind jesse
    index = 0
    for their_tickets in tickets:
        if index < jesses_place:
            if their_tickets < jesses_tickets:
                less += (jesses_tickets - their_tickets)
        else:
            if their_tickets < (jesses_tickets - 1):
                less += (jesses_tickets - their_tickets - 1) 
            behind += 1
        index += 1
    return (len(tickets) * jesses_tickets) - (less + behind)

print(jesse([5,3,2,1,4,3,7], 5))