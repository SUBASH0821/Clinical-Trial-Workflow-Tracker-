def check_compliance(site):
    """
    Basic compliance check for trial sites
    """
    if site["Status"] != "Active":
        return "Site not active"

    if site["Documents_Complete"] != "Yes":
        return "Missing essential documents"

    return "Compliant"
