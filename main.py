from concatinator import add_videos, combine_video


folders = [
    "35 - Client and Server Interactions",
    "36 - Authentication With NextAuth (Auth.js)",
    "37 - Mutations With Server Actions + Modern React Hooks",
    "38 - Deployment With Vercel",
    "39 - [OPTIONAL] Legacy Next.js The Pages Router",
]

for folder in folders:
    save_dir = add_videos(folder, separator=" ")
    combine_video(folder, save_dir)
