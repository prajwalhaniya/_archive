'''
https://leetcode.com/problems/accounts-merge/
'''
from collections import defaultdict, deque

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            emails = account[1:]
            first_email = emails[0]
            email_to_name[first_email] = name

            for email in emails[1:]:
                graph[first_email].add(email)
                graph[email].add(first_email)
                email_to_name[email] = name

            if first_email not in graph:
                graph[first_email] = set()

        visited = set()
        merged_accounts = []

        for email in graph:
            if email not in visited:
                stack = [email]
                visited.add(email)
                emails_in_component = []

                while stack:
                    current_email = stack.pop()
                    emails_in_component.append(current_email)

                    for neighbor in graph[current_email]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

                    
                merged_accounts.append([email_to_name[email]] + sorted(emails_in_component))

        return merged_accounts
         
        