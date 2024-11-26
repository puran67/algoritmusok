from collections import defaultdict, deque
import sys


def max_score(n, m, tunnels):
    # Gráf építése
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    for a, b, x in tunnels:
        graph[a].append((b, x))
        reverse_graph[b].append((a, x))

    # Bellman-Ford optimalizált algoritmus
    dist = [-float('inf')] * (n + 1)
    dist[1] = 0
    in_queue = [False] * (n + 1)
    queue = deque([1])
    in_queue[1] = True

    for _ in range(n):
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            in_queue[node] = False
            for neighbor, weight in graph[node]:
                if dist[node] + weight > dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
                    if not in_queue[neighbor]:
                        queue.append(neighbor)
                        in_queue[neighbor] = True

    # Jelöljük azokat a csúcsokat, amelyek érintettek egy pozitív ciklusban
    in_cycle = [False] * (n + 1)
    for node in range(1, n + 1):
        for neighbor, weight in graph[node]:
            if dist[node] + weight > dist[neighbor]:
                in_cycle[neighbor] = True

    # Ellenőrizzük az elérhetőséget
    def reachable(start, targets, graph):
        visited = [False] * (n + 1)
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor, _ in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return any(visited[target] for target in targets)

    # Ha van elérhető pozitív ciklus az 1-től n-ig
    if reachable(1, [i for i, x in enumerate(in_cycle) if x], graph) and \
            reachable(n, [i for i, x in enumerate(in_cycle) if x], reverse_graph):
        return -1

    return dist[n]


# Beolvasás
def main():
    input = sys.stdin.read
    data = input().splitlines()

    # Első sor: n és m
    n, m = map(int, data[0].split())

    # Következő sorok: alagutak adatai
    tunnels = []
    for line in data[1:]:
        a, b, x = map(int, line.split())
        tunnels.append((a, b, x))

    # Eredmény kiszámítása és kiírása
    result = max_score(n, m, tunnels)
    print(result)


if __name__ == "__main__":
    main()
