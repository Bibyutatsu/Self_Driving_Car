import pymunk


def create_level_1(space, HEIGHT, WIDTH, THICKNESS, STROKE):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    segment_1 = pymunk.Segment(
        body,
        (THICKNESS, HEIGHT - THICKNESS),
        (THICKNESS, HEIGHT - 2 * THICKNESS),
        STROKE)
    segment_2 = pymunk.Segment(
        body,
        (THICKNESS, HEIGHT - 2 * THICKNESS),
        (WIDTH // 4, HEIGHT - 2 * THICKNESS),
        STROKE)
    segment_3 = pymunk.Segment(
        body,
        (WIDTH // 4, HEIGHT - 2 * THICKNESS),
        (WIDTH // 2 - THICKNESS, HEIGHT // 2),
        STROKE)
    segment_4 = pymunk.Segment(
        body,
        (WIDTH // 2 - THICKNESS, HEIGHT // 2),
        (WIDTH // 2 - THICKNESS, THICKNESS),
        STROKE)
    segment_5 = pymunk.Segment(
        body,
        (WIDTH // 2 - THICKNESS, THICKNESS),
        (WIDTH - THICKNESS, THICKNESS),
        STROKE)
    segment_6 = pymunk.Segment(
        body,
        (WIDTH - THICKNESS, THICKNESS),
        (WIDTH - THICKNESS, 2 * THICKNESS),
        STROKE)
    segment_7 = pymunk.Segment(
        body,
        (WIDTH - THICKNESS, 2 * THICKNESS),
        (WIDTH // 2, 2 * THICKNESS),
        STROKE)
    segment_8 = pymunk.Segment(
        body,
        (WIDTH // 2, 2 * THICKNESS),
        (WIDTH // 2, HEIGHT // 2 + THICKNESS),
        STROKE)
    segment_9 = pymunk.Segment(
        body,
        (WIDTH // 2, HEIGHT // 2 + THICKNESS),
        (WIDTH // 4, HEIGHT - THICKNESS),
        STROKE)
    segment_10 = pymunk.Segment(
        body,
        (WIDTH // 4, HEIGHT - THICKNESS),
        (THICKNESS, HEIGHT - THICKNESS),
        STROKE)

    segment_1.collision_type = 1
    segment_2.collision_type = 1
    segment_3.collision_type = 1
    segment_4.collision_type = 1
    segment_5.collision_type = 1
    segment_6.collision_type = 1
    segment_7.collision_type = 1
    segment_8.collision_type = 1
    segment_9.collision_type = 1
    segment_10.collision_type = 1

    space.add(body,
              segment_1,
              segment_2,
              segment_3,
              segment_4,
              segment_5,
              segment_6,
              segment_7,
              segment_8,
              segment_9,
              segment_10
              )

    environment = [segment_1, segment_2, segment_3, segment_4,
                   segment_5, segment_6, segment_7, segment_8,
                   segment_9, segment_10]
    return environment
