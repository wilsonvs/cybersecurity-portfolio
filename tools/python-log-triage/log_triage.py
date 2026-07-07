#!/usr/bin/env python3
"""Summarize authentication events for basic SOC triage."""

import csv
import sys
from collections import Counter, defaultdict

FAILED_EVENT_ID = "4625"
SUCCESS_EVENT_ID = "4624"
REVIEW_THRESHOLD = 3


def load_events(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def summarize(events):
    failed = [event for event in events if event.get("event_id") == FAILED_EVENT_ID]
    successful = [event for event in events if event.get("event_id") == SUCCESS_EVENT_ID]
    failed_by_user = Counter(event.get("user", "unknown") for event in failed)
    review_users = sorted(user for user, count in failed_by_user.items() if count >= REVIEW_THRESHOLD)
    return failed, successful, failed_by_user, review_users


def build_review_notes(events, review_users):
    events_by_user = defaultdict(list)
    for event in events:
        events_by_user[event.get("user", "unknown")].append(event)

    notes = []
    for user in review_users:
        user_events = events_by_user[user]
        sources = sorted({event.get("source_ip", "unknown") for event in user_events})
        has_success = any(event.get("event_id") == SUCCESS_EVENT_ID for event in user_events)
        if has_success:
            notes.append(
                f"[MEDIUM] {user} had repeated failures followed by a success from {', '.join(sources)}"
            )
        else:
            notes.append(f"[MEDIUM] {user} had repeated failures from {', '.join(sources)}")
    return notes


def main():
    if len(sys.argv) != 2:
        print("Usage: python log_triage.py sample_events.csv")
        return 1

    events = load_events(sys.argv[1])
    failed, successful, failed_by_user, review_users = summarize(events)

    print("Authentication Summary")
    print(f"Failed logons: {len(failed)}")
    print(f"Successful logons: {len(successful)}")
    print("\nFailed logons by user:")
    for user, count in failed_by_user.most_common():
        print(f"- {user}: {count}")

    if review_users:
        print(f"\nUsers requiring review: {', '.join(review_users)}")
        print()
        for note in build_review_notes(events, review_users):
            print(note)
    else:
        print("\nUsers requiring review: none")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
