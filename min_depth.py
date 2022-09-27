import copy


def find_sibling(all_lines, line):
    parent = line[0]
    siblings = []
    for i in all_lines:
        if parent == i[0] and i != line and len(i) > 1:
            siblings.append(i)
        if len(siblings) > 0:
            return siblings[-1][1]


def find_min_depth(input_file):
    graph = {}
    with open(input_file) as f:
        all_lines = f.readlines()
        all_lines = [line.strip().split(', ') for line in all_lines]
        all_lines_copy = copy.deepcopy(all_lines)
        for line in all_lines_copy:
            if len(line) > 1:
                if line[0] not in graph.keys():
                    sibling_key = find_sibling(all_lines, line)
                    val = copy.deepcopy(graph[sibling_key])
                    val.pop()
                    val.append(line[1])
                    graph[line[1]] = val

                else:
                    graph[line[0]].append(line[1])
                    graph[line[1]] = graph.pop(line[0])
            else:
                graph[line[0]] = [line[0]]
            print(graph)

    graph_len = [len(obj) for obj in graph.values()]
    min_height = min(graph_len)
    min_depth_index = graph_len.index(min_height)
    with open('output.txt', 'w') as f:
        f.write(str(list(graph.values())[min_depth_index]))


if __name__ == '__main__':
    find_min_depth('input.txt')
