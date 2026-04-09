import platform
import os
import psutil

def get_environment_info():
    """Detects the operating environment and identifies if it's Termux or a restricted mobile context."""
    info = {
        "os": platform.system(),
        "arch": platform.machine(),
        "is_termux": "TERMUX_VERSION" in os.environ,
        "is_mobile": "ANDROID_ROOT" in os.environ or "TERMUX_VERSION" in os.environ,
        "cores": os.cpu_count(),
        "total_ram_gb": round(psutil.virtual_memory().total / (1024**3), 2),
        "available_ram_gb": round(psutil.virtual_memory().available / (1024**3), 2)
    }
    
    # Determine Intelligence Mode based on hardware
    if info["is_mobile"] or info["total_ram_gb"] < 6:
        info["suggested_mode"] = "AETHER_LITE"
        info["suggested_models"] = ["gemma-2b", "phi-4-mini", "llama-3-8b"]
    else:
        info["suggested_mode"] = "AETHER_HUB"
        info["suggested_models"] = ["strategic-deep-logic", "phi-4", "gemma-9b"]
        
    return info

def print_hardware_report():
    info = get_environment_info()
    print("🌌 [AetherNexus] Environment Intelligence Report")
    print("-" * 45)
    print(f"OS/Arch:      {info['os']} / {info['arch']}")
    print(f"Environment:  {'Termux (Mobile)' if info['is_termux'] else 'Standard Node'}")
    print(f"RAM Status:   Available: {info['available_ram_gb']}GB / Total: {info['total_ram_gb']}GB")
    print(f"Cores:        {info['cores']}")
    print("-" * 45)
    print(f"Recommended:  {info['suggested_mode']}")
    print(f"Best Models:  {', '.join(info['suggested_models'])}")
    print("-" * 45)

if __name__ == "__main__":
    print_hardware_report()
