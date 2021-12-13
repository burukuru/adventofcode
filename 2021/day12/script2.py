import logging
from pprint import pprint

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()


def find_edges(data):
    edges = {}
    for line in data:
        node_from, node_to = line.split("-")
        edges.setdefault(node_from, []).append(node_to)
        edges.setdefault(node_to, []).append(node_from)
    return edges


def follow_path(edges, start_node, visited={"start": 1}):
    paths = []
    logging.debug("===start=== %s", start_node)
    logging.debug("to_nodes %s", edges[start_node])
    for to_node in edges[start_node]:
        logging.debug("to_node %s", to_node)
        path = []
        path.append(start_node)
        visited_loop = visited.copy()
        if to_node == "end":
            path.append(to_node)
            paths.append(path)
        elif to_node == "start":
            continue
        elif to_node in visited and sorted(visited_loop.values())[-1] >= 2:
            logging.debug("already visited %s", to_node)
            continue
        elif to_node.islower():
            logging.debug("added %s to visited", to_node)
            logger.debug("following paths from %s", to_node)
            logging.debug("visited %s", visited)
            if to_node not in visited_loop:
                visited_loop[to_node] = 1
            else:
                visited_loop[to_node] += 1
            for p in follow_path(edges, to_node, visited_loop.copy()):
                paths.append(path + p)
        else:
            logger.debug("following paths from %s", to_node)
            logging.debug("visited %s", visited)
            for p in follow_path(edges, to_node, visited_loop.copy()):
                paths.append(path + p)

    logger.debug("paths %s", paths)
    logging.debug("===end=== %s", start_node)

    return paths


def main():
    edges = {}
    with open("input", encoding="utf-8") as file:
        data = file.read().splitlines()
        edges = find_edges(data)
        pprint(edges)

    paths = follow_path(edges, "start")
    pprint(paths)
    print(len(paths))


if __name__ == "__main__":
    main()
