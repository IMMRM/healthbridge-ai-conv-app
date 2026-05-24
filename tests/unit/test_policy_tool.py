# tests/unit/test_policy_tool.py

from tools.db import SessionLocal

from tools.policy_tool import (
    get_policy_by_id,
    get_policies_by_member,
    get_policies_by_plan,
    check_policy_active,
    get_remaining_sum
)


# =====================================================
# DB SESSION
# =====================================================

db = SessionLocal()


# =====================================================
# TEST 1 - GET POLICY BY ID
# =====================================================

policy = get_policy_by_id(
    db,
    "POL001"
)

print("\nTEST 1 - GET POLICY BY ID")
print(policy)


# =====================================================
# TEST 2 - GET POLICIES BY MEMBER
# =====================================================

member_policies = get_policies_by_member(
    db,
    "MEM001"
)

print("\nTEST 2 - GET POLICIES BY MEMBER")
print(member_policies)


# =====================================================
# TEST 3 - GET POLICIES BY PLAN
# =====================================================

plan_policies = get_policies_by_plan(
    db,
    "PLN002"
)
print("\nTEST 3 - GET POLICIES BY PLAN")
print(plan_policies)


# =====================================================
# TEST 4 - CHECK POLICY ACTIVE
# =====================================================

is_active = check_policy_active(
    db,
    "POL001"
)

print("\nTEST 4 - CHECK POLICY ACTIVE")
print(is_active)


# =====================================================
# TEST 5 - GET REMAINING SUM
# =====================================================

remaining_sum = get_remaining_sum(
    db,
    "POL001"
)

print("\nTEST 5 - GET REMAINING SUM")
print(remaining_sum)


# =====================================================
# CLOSE DB SESSION
# =====================================================

db.close()