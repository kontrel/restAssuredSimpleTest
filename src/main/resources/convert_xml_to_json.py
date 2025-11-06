#!/usr/bin/env python3
import xmltodict
import json
import glob
import os

def convert_junit_xml_to_json(xml_folder, output_file):
    results = []

    # Szukamy wszystkich XML z raportami Surefire
    for file in glob.glob(os.path.join(xml_folder, "*.xml")):
        with open(file, "r", encoding="utf-8") as f:
            try:
                xml_data = xmltodict.parse(f.read())
                test_suite = xml_data.get("testsuite", {})
                suite_name = test_suite.get("@name", "unknown_suite")

                suite_info = {
                    "suite_name": suite_name,
                    "tests": int(test_suite.get("@tests", 0)),
                    "failures": int(test_suite.get("@failures", 0)),
                    "errors": int(test_suite.get("@errors", 0)),
                    "skipped": int(test_suite.get("@skipped", 0)),
                    "time": float(test_suite.get("@time", 0.0)),
                    "testcases": []
                }

                # Iteracja po poszczególnych testach
                for case in test_suite.get("testcase", [] if test_suite.get("testcase") else []):
                    if isinstance(case, dict):
                        test_case = {
                            "name": case.get("@name", ""),
                            "classname": case.get("@classname", ""),
                            "time": float(case.get("@time", 0.0)),
                            "status": "PASS"
                        }

                        if "failure" in case:
                            test_case["status"] = "FAIL"
                            test_case["failure_message"] = (
                                case["failure"].get("@message", "")
                                if isinstance(case["failure"], dict)
                                else str(case["failure"])
                            )
                        elif "error" in case:
                            test_case["status"] = "ERROR"
                        elif "skipped" in case:
                            test_case["status"] = "SKIPPED"

                        suite_info["testcases"].append(test_case)

                results.append(suite_info)

            except Exception as e:
                print(f"Błąd przy parsowaniu {file}: {e}")

    with open(output_file, "w", encoding="utf-8") as out:
        json.dump(results, out, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    convert_junit_xml_to_json("target/surefire-reports", "test-results.json")
    print("✅ Raport testów zapisany jako test-results.json")
