import json
SHA="a"*40
CONDITIONAL=json.dumps({"verdict":"CONDITIONAL","primary_risk":"NOTICE","evidence_score":92,"evidence_band":"HIGH","obligations_mask":3,"blocker_count":0,"condition_count":1,"evidence_gap":"NONE","explanation":"The MIT release is usable in SaaS if copyright and permission notices are preserved."})
INCOMPATIBLE=json.dumps({"verdict":"INCOMPATIBLE","primary_risk":"COPYLEFT","evidence_score":90,"evidence_band":"HIGH","obligations_mask":12,"blocker_count":1,"condition_count":0,"evidence_gap":"NONE","explanation":"A GPL-only dependency conflicts with the submitted closed binary distribution policy."})
MISSING=json.dumps({"verdict":"INSUFFICIENT_EVIDENCE","primary_risk":"UNKNOWN","evidence_score":20,"evidence_band":"LOW","obligations_mask":0,"blocker_count":0,"condition_count":0,"evidence_gap":"LICENSE_MISSING","explanation":"No pinned license text is available, so compatibility cannot be established safely."})
def deploy(direct_deploy):return direct_deploy("contract.py",sdk_version="v0.2.12")
def request(c,model="COMMERCIAL_SAAS"):c.request_audit("expressjs/express",SHA,"5.1.0","NPM","package.json",model)
def evidence(vm):vm.mock_web(r".*raw\.githubusercontent\.com.*",{"status":200,"body":"MIT License. Copyright notice and permission notice shall be included."})
def test_requires_sha(direct_vm,direct_deploy):
 c=deploy(direct_deploy)
 with direct_vm.expect_revert("Full commit SHA"):c.request_audit("a/b","main","1","NPM","package.json","COMMERCIAL_SAAS")
def test_request(direct_deploy):c=deploy(direct_deploy);request(c);assert c.get_audit(0).status=="PENDING"
def test_conditional_notice(direct_vm,direct_deploy):
 evidence(direct_vm);direct_vm.mock_llm(r".*",CONDITIONAL);c=deploy(direct_deploy);request(c);c.audit_release(0);assert c.get_passport(0).status=="CONDITIONS_REQUIRED";assert direct_vm.run_validator()is True
def test_gpl_blocked(direct_vm,direct_deploy):
 evidence(direct_vm);direct_vm.mock_llm(r".*",INCOMPATIBLE);c=deploy(direct_deploy);request(c,"CLOSED_BINARY");c.audit_release(0);assert c.get_passport(0).status=="BLOCKED"
def test_missing_fails_closed(direct_vm,direct_deploy):
 evidence(direct_vm);direct_vm.mock_llm(r".*",MISSING);c=deploy(direct_deploy);request(c);c.audit_release(0);assert c.get_passport(0).status=="EVIDENCE_REQUIRED"
def test_no_second_finalization(direct_vm,direct_deploy):
 evidence(direct_vm);direct_vm.mock_llm(r".*",CONDITIONAL);c=deploy(direct_deploy);request(c);c.audit_release(0)
 with direct_vm.expect_revert("already finalized"):c.audit_release(0)
