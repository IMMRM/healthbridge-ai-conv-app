# tests/unit/test_policy_tool.py

from unittest.mock import MagicMock

from models.policies import Policy

from tools.policy_tool import (
    get_policy_by_id,
    get_policies_by_member,
    get_policies_by_plan,
    check_policy_active,
    get_remaining_sum
)


# =====================================================
# TEST 1
# GET POLICY BY ID
# =====================================================

def test_get_policy_by_id():

    policy = Policy()

    policy.policy_id = "POL001"

    policy.plan_id = "HERO"

    policy.policy_holder_id = "MEM001"

    policy.sum_assured = 500000

    policy.premium = 12000

    policy.remaining_sum = 420000

    policy.status = "active"

    policy.start_date = None

    policy.end_date = None


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .first.return_value
    ) = policy


    result = get_policy_by_id(
        mock_db,
        "POL001"
    )


    assert result["policy_id"] == "POL001"

    assert result["plan_id"] == "HERO"

    assert result["sum_assured"] == 500000.0

    assert result["status"] == "active"


# =====================================================
# TEST 2
# GET POLICIES BY MEMBER
# =====================================================

def test_get_policies_by_member():

    policy1 = Policy()

    policy1.policy_id = "POL001"

    policy1.policy_holder_id = "MEM001"

    policy1.plan_id = "HERO"


    policy2 = Policy()

    policy2.policy_id = "POL002"

    policy2.policy_holder_id = "MEM001"

    policy2.plan_id = "STAR"


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .all.return_value
    ) = [policy1, policy2]


    result = get_policies_by_member(
        mock_db,
        "MEM001"
    )


    assert len(result) == 2

    assert result[0]["policy_id"] == "POL001"

    assert result[1]["policy_id"] == "POL002"


# =====================================================
# TEST 3
# GET POLICIES BY PLAN
# =====================================================

def test_get_policies_by_plan():

    policy = Policy()

    policy.policy_id = "POL010"

    policy.plan_id = "SUPERSTAR"

    policy.policy_holder_id = "MEM010"


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .all.return_value
    ) = [policy]


    result = get_policies_by_plan(
        mock_db,
        "SUPERSTAR"
    )


    assert len(result) == 1

    assert result[0]["plan_id"] == "SUPERSTAR"


# =====================================================
# TEST 4
# CHECK POLICY ACTIVE
# =====================================================

def test_check_policy_active():

    policy = Policy()

    policy.policy_id = "POL001"

    policy.status = "active"


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .first.return_value
    ) = policy


    result = check_policy_active(
        mock_db,
        "POL001"
    )


    assert result is True


# =====================================================
# TEST 5
# CHECK POLICY INACTIVE
# =====================================================

def test_check_policy_inactive():

    policy = Policy()

    policy.policy_id = "POL002"

    policy.status = "expired"


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .first.return_value
    ) = policy


    result = check_policy_active(
        mock_db,
        "POL002"
    )


    assert result is False


# =====================================================
# TEST 6
# GET REMAINING SUM
# =====================================================

def test_get_remaining_sum():

    policy = Policy()

    policy.policy_id = "POL001"

    policy.remaining_sum = 350000


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .first.return_value
    ) = policy


    result = get_remaining_sum(
        mock_db,
        "POL001"
    )


    assert result == 350000.0