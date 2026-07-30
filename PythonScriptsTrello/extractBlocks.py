#extractBlocks
import re
import json

LINE = re.compile(r'^- \[( |x)\] (\S+) · (\w+) · (\S+) — (.+)$')

def parse_backlog(path="./backlog.md"):
    blocks = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = LINE.match(line.rstrip("\n"))
            if m:
                done, block_id, track, size, desc = m.groups()
                blocks.append({
                    "id": block_id,
                    "track": track,
                    "size": size,
                    "done": done == "x",
                    "description": desc,
                })
    return blocks

SECTION = re.compile(r'^## Pulled\s*$')
NEXT_SECTION = re.compile(r'^## ')
ID_LINE = re.compile(r'^([\w-]+)\s*$')



SECTION = re.compile(r'^## Pulled\s*$')
NEXT_SECTION = re.compile(r'^## ')
ID_LINE = re.compile(r'^([\w-]+)\s*$')


def parse_week(path="./week.md"):
    ids = []
    in_section = False
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if SECTION.match(line):
                in_section = True
                continue
            if in_section and NEXT_SECTION.match(line):
                break
            if in_section:
                m = ID_LINE.match(line)
                if m:
                    ids.append(m.group(1))
    return ids


def current_week_tasks(week_path="./week.md", backlog_path="./backlog.md"):
    week_ids = parse_week(week_path)
    backlog = {b["id"]: b for b in parse_backlog(backlog_path)}
    return [backlog[i] for i in week_ids if i in backlog]


if __name__ == "__main__":
    tasks = current_week_tasks()
    print(json.dumps(tasks, sort_keys=True, indent=4, separators=(",", ": ")))


#SchedualBlocks = parse_backlog("week.md")

#json_str = json.dumps(SchedualBlocks)

#print(type(json_str))
#print("Json List::", json_str)
#print(json.dumps(json.loads(json_str), sort_keys=True, indent=4, separators=(",", ": ")))



