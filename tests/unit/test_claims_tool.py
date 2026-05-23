from tools.db import SessionLocal

from tools.claims_tool import (
    get_claim_by_id,
    get_claim_breakup_by_claim_id,
    get_claims_by_member_id,
    get_recent_claims,
    update_claim_status
)

db = SessionLocal()


# ---------------------------------------------------
# TEST 1
# ---------------------------------------------------

claim = get_claim_by_id(db, "CLM001")

print("\nTEST 1 - GET CLAIM")
print(claim)


# ---------------------------------------------------
# TEST 2
# ---------------------------------------------------

breakup = get_claim_breakup_by_claim_id(
    db,
    "CLM001"
)

print("\nTEST 2 - CLAIM BREAKUP")
print(breakup)


# ---------------------------------------------------
# TEST 3
# ---------------------------------------------------

member_claims = get_claims_by_member_id(
    db,
    "MEM001"
)

print("\nTEST 3 - MEMBER CLAIMS")
print(member_claims)


# ---------------------------------------------------
# TEST 4
# ---------------------------------------------------

recent_claims = get_recent_claims(db)

print("\nTEST 4 - RECENT CLAIMS")
print(recent_claims)


# ---------------------------------------------------
# TEST 5
# ---------------------------------------------------

updated_claim = update_claim_status(
    db,
    "CLM001",
    "under_review"
)

print("\nTEST 5 - UPDATE STATUS")
print(updated_claim)


db.close()