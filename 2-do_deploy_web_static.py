from fabric.api import env, put, run
import os

# Define the IPs of your web servers
env.hosts = ['54.175.222.189', '54.157.184.160']

def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract the filename without extension
        archive_filename = archive_path.split('/')[-1]
        archive_folder = archive_filename.split('.')[0]

        # Upload the archive to /tmp/ directory on the server
        put(archive_path, '/tmp/{}'.format(archive_filename))

        # Create target directory
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_folder))

        # Uncompress the archive to the target directory
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_filename, archive_folder))

        # Delete the uploaded archive from the server
        run('rm /tmp/{}'.format(archive_filename))

        # Move contents out of the web_static folder
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(archive_folder, archive_folder))

        # Remove the now empty web_static folder
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_folder))

        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the new version
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_folder))

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
