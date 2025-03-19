Following these steps, you should have Dependency-Track running smoothly on Docker with a PostgreSQL database for production use. For more detailed configuration options, refer to the [official Dependency-Track documentation](https://docs.dependencytrack.org/).

1. **Dependency-Track Docker Image**

By default, **Dependency-Track** runs with an embedded **H2** database, which is suitable for testing and development purposes. However, for **production environments**, it is highly recommended to use a **PostgreSQL** database to ensure better scalability and stability.

---

2. **Setting up Dependency-Track using Docker Compose**

Clone my repository:

```bash
git clone https://github.com/ArcElewyn/IT.git
cd IT/Dependency-Track/Docker
```

3. **Configuration**

Adjust the content of the docker-compose.yml to match your setup

4. **Run the container**
```bash
docker compose up -d
```

5. **Verify the installation**
```bash
docker ps -a 
```
If it is not running, 
```bash
docker start dependency-track
```

Then login via the web page

*http://ipofyourserver:8080*

Default login credentials: admin / admin

1. **Metrics**
You can enable Prometheus metrics by uncommenting the relevant lines in the docker-compose.yml file.


