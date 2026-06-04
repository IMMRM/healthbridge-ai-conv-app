from unittest.mock import MagicMock

from models.claims import Claim
from models.claims_breakup import ClaimsBreakup

from tools.claims_tool import (
    get_claim_by_id,
    get_claim_breakup_by_claim_id,
    get_claims_by_member_id,
    get_claims_by_policy_id,
    get_recent_claims,
    update_claim_status
)


# =====================================================
# TEST 1
# GET CLAIM BY ID
# =====================================================

def test_get_claim_by_id():

    mock_claim = Claim()

    mock_claim.claim_id = "CLM001"
    mock_claim.policy_id = "POL001"
    mock_claim.member_id = "MEM001"

    mock_claim.claim_amount = 50000
    mock_claim.approved_amount = 45000

    mock_claim.status = "approved"

    mock_claim.hospital_name = "City Hospital"

    mock_claim.claim_type = "cashless"

    mock_claim.claim_date = None


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .first.return_value
    ) = mock_claim


    result = get_claim_by_id(
        mock_db,
        "CLM001"
    )


    assert result["claim_id"] == "CLM001"

    assert result["claim_amount"] == 50000.0

    assert result["status"] == "approved"


# =====================================================
# TEST 2
# GET CLAIM BREAKUP
# =====================================================

def test_get_claim_breakup_by_claim_id():

    breakup = ClaimsBreakup()

    breakup.breakup_id = "BR001"

    breakup.claim_id = "CLM001"

    breakup.benefit_type = "room_rent"

    breakup.sub_type = "private_room"

    breakup.amount = 10000

    breakup.approved_amount = 8000

    breakup.remarks = "Room cap exceeded"


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .all.return_value
    ) = [breakup]


    result = get_claim_breakup_by_claim_id(
        mock_db,
        "CLM001"
    )


    assert len(result) == 1

    assert result[0]["benefit_type"] == "room_rent"

    assert result[0]["approved_amount"] == 8000.0


# =====================================================
# TEST 3
# GET CLAIMS BY MEMBER
# =====================================================

def test_get_claims_by_member_id():

    claim1 = Claim()
    claim1.claim_id = "CLM001"
    claim1.member_id = "MEM001"
    claim1.claim_amount = 50000
    claim1.approved_amount = 40000
    claim1.status = "approved"

    claim2 = Claim()
    claim2.claim_id = "CLM002"
    claim2.member_id = "MEM001"
    claim2.claim_amount = 25000
    claim2.approved_amount = 20000
    claim2.status = "approved"


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .order_by.return_value
        .all.return_value
    ) = [claim1, claim2]


    result = get_claims_by_member_id(
        mock_db,
        "MEM001"
    )


    assert len(result) == 2

    assert result[0]["claim_id"] == "CLM001"

    assert result[1]["claim_id"] == "CLM002"


# =====================================================
# TEST 4
# GET CLAIMS BY POLICY
# =====================================================

def test_get_claims_by_policy_id():

    claim = Claim()

    claim.claim_id = "CLM010"

    claim.policy_id = "POL001"

    claim.claim_amount = 90000

    claim.approved_amount = 70000

    claim.status = "approved"


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .order_by.return_value
        .all.return_value
    ) = [claim]


    result = get_claims_by_policy_id(
        mock_db,
        "POL001"
    )


    assert len(result) == 1

    assert result[0]["policy_id"] == "POL001"


# =====================================================
# TEST 5
# GET RECENT CLAIMS
# =====================================================

def test_get_recent_claims():

    claim = Claim()

    claim.claim_id = "CLM100"

    claim.claim_amount = 100000

    claim.approved_amount = 80000

    claim.status = "approved"


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .order_by.return_value
        .limit.return_value
        .all.return_value
    ) = [claim]


    result = get_recent_claims(
        mock_db,
        limit=1
    )


    assert len(result) == 1

    assert result[0]["claim_id"] == "CLM100"


# =====================================================
# TEST 6
# UPDATE CLAIM STATUS
# =====================================================

def test_update_claim_status():

    claim = Claim()

    claim.claim_id = "CLM001"

    claim.status = "initiated"


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .first.return_value
    ) = claim


    result = update_claim_status(
        mock_db,
        "CLM001",
        "approved"
    )


    assert result["status"] == "approved"

    mock_db.commit.assert_called_once()

    mock_db.refresh.assert_called_once()