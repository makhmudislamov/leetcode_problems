"""
# ---------------------------------------------------------------------------- #
#                             Subdomain Visit Count                            #
# ---------------------------------------------------------------------------- #
A website domain like "discuss.leetcode.com" consists of various subdomains:
    - At the top level, we have "com".
    - At the next level, we have "leetcode.com".
    - At the lowest level, "discuss.leetcode.com".
When we visit a domain like "discuss.leetcode.com", we will visit the parent
domains "leetcode.com" and "com" implicitly.
This problem defines a "count-paired domain" to be a count representing the
number of visits this domain received, followed by a space, followed by the address.
An example of a count-paired domain might be `9001 discuss.leetcode.com`.
- Given a list `cpdomains` of count-paired domains .
- Return a list count-paired domains, explicitly counting the number of visits to each subdomain.
    - Should be in the same format as the input.
    - Can be returned in any order.
# ---------------------------------------------------------------------------- #
# --------------------------------- EXAMPLE 1 -------------------------------- #
- Input:  ["9001 discuss.leetcode.com"]
- Output: ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
-Explaination:
    We only have one website domain: "discuss.leetcode.com".
    As mentioned above, subdomains "leetcode.com" and "com" are also visited,
    so they will all be visited 9001 times.
# --------------------------------- EXAMPLE 2 -------------------------------- #
- Input:  ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
- Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
- Explaination:
    We will visit "google.mail.com" 900 times, "yahoo.com" 50 times,
    "intel.mail.com" once and "wiki.org" 5 times.
    For the subdomains, we will visit "mail.com" 900 + 1 = 901 times,
    "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
# ----------------------------------- NOTES ---------------------------------- #
- The length of `cpdomains` will not exceed `100`.
- The length of each domain name will not exceed `100`.
- Each address will have either 1 or 2 `.` characters.
- The input count in any count-paired domain will not exceed `10000`.
- The answer output can be returned in any order.
# ---------------------------------------------------------------------------- #
"""


# - Input:  ["9001 discuss.leetcode.com"]
# - Output: ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]

def visit_count(input):

        # iterating over the input
        # splitting >> list (2 items): "count" "full dom"
        # split full domain
        # translate num (str) to int
        # increment count
    for domain in input:
        domain = domain.split() # list

        count = int(domain[0])
        full_dom = domain[1]
        # print("count", count, "dom", full_dom)

        full_dom = full_dom.split(".")
        # print("full", full_dom)

        for sub in full_dom:
            if sub in input:
                count += 1
        
        # print(count)
        


        





       




input = ["9001 discuss.leetcode.com"]
print(visit_count(input))
