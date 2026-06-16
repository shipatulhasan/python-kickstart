# Change these values to verify different execution paths!
is_active = True
cpu_percent = 84.5
is_production = True
should_alert = False

# TODO: Build your compound logical matching condition statement
if not is_active:
    should_alert=True;
elif cpu_percent>90.0 and is_production:
    should_alert=True;

if should_alert:
    print("[ALERT] Urgent dispatch! System needs manual intervention.")
else:
    print("[OK] System operating within safe margin bounds.")