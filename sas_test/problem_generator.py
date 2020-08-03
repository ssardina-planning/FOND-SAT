import optparse


# To run the script, just execute ./problem_genetator.py -s SIZE, where SIZE is an integer


parser = optparse.OptionParser()
parser.add_option('-s', '--size', action='store', dest='size',
                      help='size of the corridor, i.e., number of cells',
                      default=3)

options, args = parser.parse_args()

size = int(options.size)

# Update domain
domain_file = open('generalized_domain.pddl','r')
new_problem = []
for line in domain_file:
    if ':constants' in line:
        new_line = '(:constants '
        for x in range(size):
            new_line += 'c' + str(x) + ' '
        new_line += '- Cell)\n'
        new_problem.append(new_line)
    else:
        new_problem.append(line)
domain_file.close()
outfile = open('generalized_domain.pddl','w')
for line in new_problem:
    outfile.write(line)
outfile.close()

# Update problem
problem_file = open('generalized_problem.pddl','w')
problem_file.write('(define (problem p1)\n(:domain no_running_1)\n(:init\n')
for x in range(size-1):
    problem_file.write('(right c' + str(x) + ' c' + str(x+1) + ')\n')
    problem_file.write('(left c' + str(x+1) + ' c' + str(x) + ')\n')
# Initial state of the agent, in case you want to change it
problem_file.write('(at c0)\n)\n')
# Goal state of the agent, in case you want to change it
problem_file.write('(:goal\n(at c' + str(size-1) + ')\n)\n)')
problem_file.close()

print('Planning task generated for a corridor of size ' + str(size) + '!')