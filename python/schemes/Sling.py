payload = loadBody('json')
payload['message'] = list(cdm.service_certificate_challenge)
service_cert = await corsFetch(licUrl, "POST", licHeaders, payload, "blob")
payload['message'] = list(getChallenge('list', service_cert))
licence = await corsFetch(licUrl, "POST", licHeaders, payload, "blob")
