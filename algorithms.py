def fcfs(requests, head):
    order = [head] + requests[:]
    movement = 0
    for i in range(1, len(order)):
        movement += abs(order[i] - order[i-1])
    return order, movement


def sstf(requests, head):
    reqs = requests[:]
    pos = head
    order = [head]
    movement = 0
    while reqs:
        nearest = min(reqs, key=lambda x: abs(x - pos))
        movement += abs(nearest - pos)
        pos = nearest
        order.append(pos)
        reqs.remove(nearest)
    return order, movement


def scan(requests, head, disk_size, direction='up'):
    reqs = sorted(requests)
    order = [head]
    movement = 0
    left = [r for r in reqs if r < head]
    right = [r for r in reqs if r >= head]

    if direction == 'up':
        for r in right:
            movement += abs(r - order[-1])
            order.append(r)

        if order[-1] != disk_size - 1:
            movement += abs((disk_size - 1) - order[-1])
            order.append(disk_size - 1)

        for r in reversed(left):
            movement += abs(order[-1] - r)
            order.append(r)
    else:
        for r in reversed(left):
            movement += abs(r - order[-1])
            order.append(r)

        if order[-1] != 0:
            movement += abs(order[-1] - 0)
            order.append(0)

        for r in right:
            movement += abs(order[-1] - r)
            order.append(r)

    return order, movement


def cscan(requests, head, disk_size, direction='up'):
    reqs = sorted(requests)
    order = [head]
    movement = 0
    left = [r for r in reqs if r < head]
    right = [r for r in reqs if r >= head]

    if direction == 'up':
        for r in right:
            movement += abs(r - order[-1])
            order.append(r)

        if order[-1] != disk_size - 1:
            movement += abs((disk_size - 1) - order[-1])
            order.append(disk_size - 1)

        movement += (disk_size - 1)
        order.append(0)

        for r in left:
            movement += abs(r - order[-1])
            order.append(r)
    else:
        for r in reversed(left):
            movement += abs(r - order[-1])
            order.append(r)

        if order[-1] != 0:
            movement += abs(order[-1] - 0)
            order.append(0)

        movement += (disk_size - 1)
        order.append(disk_size - 1)

        for r in reversed(right):
            movement += abs(order[-1] - r)
            order.append(r)

    return order, movement


def parse_requests(text):
    parts = text.replace(',', ' ').split()
    return [int(p) for p in parts]
