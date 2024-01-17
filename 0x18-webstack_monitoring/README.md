0x18. Webstack monitoring
-------------------------

**0. Sign up for Datadog and install datadog-agent** >> Signing up for a free `Datadog` account on the US website of [Datadog](https://www.datadoghq.com/), using the **US1** region. Afterward, `datadog-agent` is installed on `web-01`, and an `application key` created that the server then be visible under the host name `XX-web-01` (Validate using the [this API](https://docs.datadoghq.com/api/latest/hosts/)). The DataDog `API key` and DataDog `application key` is then copied into the intranet user profile ([here](https://intranet.alxswe.com/users/my_profile)). Hostname of the server updated as need be.

**1. Monitor some metrics** >> Setting up monitors within the `DataDog` dashboard that checks the number of both read and write requests issued to the device per second. This system metrics info can be used to inform a company's decisions, such as how to scale. More on the various system metrics one can monitor available here: [System Check](https://docs.datadoghq.com/integrations/system/)

**2. Create a dashboard** `[2-setup_datadog]` >> Creating a new `dashboard` with at least 4 `widgets` of any type, and monitoring different metrics that are displayed in order to get a few different visualizations. The file `2-setup_datadog` has `dashboard_id` on the first line. **Note:** The dashboard `id` might need to be retrieved using [Datadog's API](https://docs.datadoghq.com/api/latest/)
