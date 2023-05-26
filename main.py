def read_graph_from_file(name):
    try:
        file = open(name, "r")
    except FileNotFoundError:
        print("Ошибка при открытии файла. Проверьте название")
        exit()
    try:
        graph = [[int(j) for j in i.split() if int(j) >= 0] for i in file.readlines()]
        for i in graph:
            if len(i) != len(graph):
                raise ValueError
    except ValueError:
        print("Ошибка! В файле находятся некорректные данные!")
        exit()
    finally:
        file.close()

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != graph[j][i]:
                print("Ошибка! Граф должен быть неориентированным")
                exit()

    return graph


def get_adj_list(graph):
    return [[j for j in range(len(graph[i])) if graph[i][j] != 0] for i in range(len(graph))]


def get_isolated_vertices_count(adj):
    return sum([1 for i in range(len(adj)) if len(adj[i]) == 0 or (len(adj[i]) == 1 and adj[i][0] == i)])


def is_graph_tree(adj, parent_index=0, current_index=0, passed_points=[]):
    if get_isolated_vertices_count(adj) != 0:
        return False
    root = adj[current_index]
    for i in root:
        if i in passed_points and i != parent_index:
            return False
        if i != parent_index:
            passed_points.extend(root)
            parent_index = current_index
            return is_graph_tree(adj, parent_index, i, passed_points)
    if len(passed_points) != len(adj):
        return False
    return True


filename = input("Введите имя файла: ")
graph = read_graph_from_file(filename)
adj = get_adj_list(graph)

isolated_vertices_count = get_isolated_vertices_count(adj)
print(f"Количество изолированных вершин: {isolated_vertices_count}")
print(f"Является деревом - {is_graph_tree(adj)}")
