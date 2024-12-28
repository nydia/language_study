FROM 172.30.41.248/base_images/spring-boot:openjdk8
ADD target/mengxiu-demo.jar /opt/appl/spring-cloud/mengxiu-demo.jar
EXPOSE 8080
CMD ["java", "-jar", "/opt/appl/spring-cloud/mengxiu-demo.jar" ,"--spring.profiles.active=dev"]