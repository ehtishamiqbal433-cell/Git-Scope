import sys
import libcst as cst

class TaintVisitor(cst.CSTVisitor):
    def __init__(self):
        self.tainted_vars = set()
        self.violations = []

    def visit_Assign(self, node: cst.Assign) -> None:
        for target in node.targets:
            if isinstance(target.target, cst.Name):
                var_name = target.target.value
                if isinstance(node.value, cst.SimpleString):
                    val = node.value.value.lower()
                    if any(secret_kw in val for secret_kw in ["sk_live_", "bearer", "password", "private_key"]):
                        self.violations.append(f"Hardcoded secret detected in variable '{var_name}'")

    def visit_Call(self, node: cst.Call) -> None:
        if isinstance(node.func, cst.Attribute):
            attr_name = node.func.attr.value
            if attr_name in ["post", "get", "request", "urlopen"]:
                for arg in node.args:
                    if isinstance(arg.value, cst.Name) and arg.value.value in self.tainted_vars:
                        self.violations.append(f"Security violation: Tainted variable '{arg.value.value}' passed to network sink '{attr_name}'")

def scan_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        code_content = f.read()
    
    try:
        module = cst.parse_module(code_content)
        visitor = TaintVisitor()
        module.visit(visitor)
        return visitor.violations
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return []

if __name__ == "__main__":
    file_path = sys.argv[1]
    issues = scan_file(file_path)
    if issues:
        for issue in issues:
            print(f"[!] {issue}")
        sys.exit(1)
    print("[+] Code clean.")
    sys.exit(0)
