from agent.self_audit_agent import SelfAuditingAgent

agent = SelfAuditingAgent(sensitivity="Medium")

report = agent.run_audit()
print("\nFINAL REPORT:\n", report)

if report["status"] == "CRITICAL":
    repair = agent.attempt_repair()
    print("\nREPAIR RESULT:\n", repair)