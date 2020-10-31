from argparse import ArgumentParser

# To run the script, just execute ./problem_genetator.py -s SIZE, where SIZE is an integer

if __name__ == '__main__':
    parser = ArgumentParser(
        description="Generates a corridor domain file generalized_domain-<size>.pddl of a given size <size>")
    parser.add_argument('size', help="size of the corridor, i.e., number of cells")
    args = parser.parse_args()

    size = int(args.size)
    pddl_domain_base = 'generalized_domain.pddl'.format(size)

    pddl_domain_size = 'generalized_domain_{}.pddl'.format(size)
    pddl_problem_size = 'generalized_problem_{}.pddl'.format(size)
    name_domain = 'no_running_{}'.format(size)
    name_problem = 'p{}'.format(size)

    # Update domain
    domain_file = open(pddl_domain_base, 'r')
    new_problem = []
    for line in domain_file:
        new_line = line
        if '(define' in line:
            new_line = '(define (domain {})'.format(name_domain)
        if ':constants' in line:
            new_line = '(:constants '
            for x in range(size):
                new_line += 'c' + str(x) + ' '
            new_line += '- Cell)\n'
        new_problem.append(new_line)

    domain_file.close()
    outfile = open(pddl_domain_size,'w')
    for line in new_problem:
        outfile.write(line)
    outfile.close()

    # Update problem
    problem_file = open(pddl_problem_size,'w')
    problem_file.write('(define (problem {})\n(:domain {})\n(:init\n'.format(name_problem, name_domain))
    for x in range(size-1):
        problem_file.write('(right c' + str(x) + ' c' + str(x+1) + ')\n')
        problem_file.write('(left c' + str(x+1) + ' c' + str(x) + ')\n')
    # Initial state of the agent, in case you want to change it
    problem_file.write('(at c0)\n)\n')
    # Goal state of the agent, in case you want to change it
    problem_file.write('(:goal\n(at c' + str(size-1) + ')\n)\n)')
    problem_file.close()

    print('Planning task generated for a corridor of size ' + str(size) + '!')